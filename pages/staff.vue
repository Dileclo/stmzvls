<template>
    <div>
        <UIPageTitle title="Сотрудники"></UIPageTitle>
        <UIButton @click="isOpen = true">Добавить</UIButton>
        <DataTable ref="table" ajax="http://127.0.0.1:8000/get_users" :columns="columns" class="display" :options="{
            scrollX: true, 
            language: {
            },
        }">
            <template #column-5="props">
                <div class="flex gap-2">
                    <UIButton @click="rowClick(props.rowData)">
                        Изменить
                    </UIButton>
                    <UIButton @click="deleteClick(props.rowData)">
                        Удалить
                    </UIButton>
                </div>
            </template>
        </DataTable>
        <UModal v-model=isOpen>
            <span class="p-5 text-xl">Добавить сотрудника</span>
            <UIDivider></UIDivider>
            <form action="" @submit.prevent="add_user" class="p-5">
                <div class="flex flex-col">
                    <label for="" class="mb-1">Фамилия</label>
                    <input class="border pl-1 rounded focus:border-blue-400 focus:outline-0" type="text"
                        v-model="user.family_name">
                </div>
                <div class="flex flex-col">
                    <label for="" class="mb-1">Имя</label>
                    <input class="border pl-1 rounded focus:border-blue-400 focus:outline-0" type="text"
                        v-model="user.name">
                </div>
                <div class="flex flex-col">
                    <label for="" class="mb-1">Отчество</label>
                    <input class="border pl-1 rounded focus:border-blue-400 focus:outline-0" type="text"
                        v-model="user.second_name">
                </div>
                <div class="flex flex-col">
                    <label for="" class="mb-1">E-Mail</label>
                    <input class="border pl-1 rounded focus:border-blue-400 focus:outline-0" type="text"
                        v-model="user.email">
                </div>
                <div class="flex flex-col">
                    <label for="" class="mb-1">Телефон</label>
                    <input class="border pl-1 rounded focus:border-blue-400 focus:outline-0" type="text"
                        v-model="user.phone">
                </div>
                <div class="flex flex-col">
                    <label for="" class="mb-1">Должность</label>
                    <input class="border pl-1 rounded focus:border-blue-400 focus:outline-0" type="text"
                        v-model="user.position">
                </div>
                <UIButton type="submit" class="mt-4">Добавить</UIButton>
            </form>
        </UModal>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net';
import 'datatables.net-select';
import 'datatables.net-responsive';
import axios from 'axios';
DataTable.use(DataTablesCore);

let dt
const toast = useToast()

const table = ref()
const isOpen = ref(false);
const user = ref({
    name: '',
    family_name: '',
    second_name:'',
    email: '',
    phone: '',
    position: ''
})
onMounted(function () {
  dt = table.value.dt;
});
function add_user(){
    console.log(user.value)
    axios.post("http://127.0.0.1:8000/add_user",user.value).then(function(res){
        toast.add({ title: 'Успешно добавлено'})
        isOpen.value = false
        dt.ajax.reload()
    }).catch(function(err){
        console.log(err)
        toast.add({title:err.response.data.detail,color:'red'})
    })
}

const data = ref([])
const columns = [
    { data: 'name', title: 'Имя' },
    { data: 'family_name', title: 'Фамилия' },
    { data: 'second_name', title: 'Отчество' },
    { data: 'email', title: 'E-Mail' },
    { data: 'phone', title: 'Телефон' },
]

function rowClick(data) {
    console.log(data)

}

function deleteClick(data) {
    console.log(data)
}


</script>
<style>
@import 'datatables.net-dt';

.dt-layout-row {
    @apply flex justify-between
}

.dt-input {
    @apply border p-1 rounded-lg
}

.dt-layout-table {
    @apply mt-4 overflow-hidden overflow-x-auto max-md:max-w-[310px] max-md:text-xs
}

.dt-info {
    @apply hidden
}

.dt-paging-button.first {
    @apply hidden !important
}

.dt-paging-button.last {
    @apply hidden !important
}
</style>