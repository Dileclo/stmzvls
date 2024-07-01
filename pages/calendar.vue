<template>
    <div>
        <UInput placeholder="Filter people..." />
        <div class="py-5 flex-col">
            <div class="ml-[69px]">
                <UButton color="white" @click="today">
                    Сегодня
                </UButton>
            </div>
            <div class="items-center flex gap-4">
                <UButton color="white" @click="prevDate">
                    <Icon class="text-black" size="24px" name="akar-icons:chevron-left" />
                </UButton>
                <UPopover :popper="{ placement: 'bottom-start' }">
                    <UButton icon="i-heroicons-calendar-days-20-solid" :label="formatDate(currentDate.value)" />

                    <template #panel="{ close }">
                        <UIDatePicker v-model="currentDate.value" is-required @close="close" />
                    </template>
                </UPopover>
                <UButton color="white" @click="nextDate">
                    <Icon class="text-black" size="24px" name="akar-icons:chevron-right" />
                </UButton>
            </div>
        </div>
        <UTable :rows="people" :columns="columns">
            <template #role-data="{ row }">
                <UCheckbox :modelValue="row.is_present" @update:modelValue="value => toggleAttendance(row, value)" />
            </template>
        </UTable>
    </div>
</template>

<script setup>
import { format } from 'date-fns';
import { ref, onMounted, computed, watch } from 'vue';
import dayjs from 'dayjs';
import axios from 'axios';
import 'dayjs/locale/ru';
import localizedFormat from 'dayjs/plugin/localizedFormat';

dayjs.extend(localizedFormat);
dayjs.locale('ru');

const people = ref([]);
const currentDate = ref(dayjs());
const formattedDate = computed(() => currentDate.value.format('MMMM D, YYYY'));

const columns = [
    { key: 'name', label: 'ФИО' },
    { key: 'position', label: 'Должность' },
    { key: 'email', label: 'Email' },
    { key: 'role' },
];

const fetchPeopleByDate = async (date) => {
    const formattedDateForAPI = date.format('YYYY-MM-DD');
    const response = await axios.get(`http://127.0.0.1:8000/get_users_by_date?date=${formattedDateForAPI}`);

    people.value = response.data.data.map(person => ({
        ...person,
        is_present: person.is_present ? true : false
    }));
};

const prevDate = () => {
    currentDate.value = currentDate.value.subtract(1, 'day');
};

const today = () => {
    currentDate.value = dayjs();
};

const nextDate = () => {
    currentDate.value = currentDate.value.add(1, 'day');
};

const formatDate = (date) => {
    return date ? date.format('D MMM, YYYY') : '';
};

const toggleAttendance = async (row, value) => {
    row.is_present = value;
    const update = {
        'user_id': row.id,
        'date': currentDate.value.format('YYYY-MM-DD'),
        'is_present': row.is_present
    };
    await axios.post('http://127.0.0.1:8000/update_attendance', update)
        .then((response) => {
            console.log(response);
        })
        .catch((error) => {
            console.error('Failed to update attendance', error);
        });
};

onMounted(() => {
    fetchPeopleByDate(currentDate.value);
});

watch(currentDate, (newDate) => {
    fetchPeopleByDate(newDate);
});
</script>
