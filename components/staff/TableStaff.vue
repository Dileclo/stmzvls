<template>
    <DataTable v-if="dataTableVisible" ref="table" ajax="http://127.0.0.1:8000/get_users" :columns="columns"
        class="display" :options="{
            scrollX: true,
            language: {
            },
            responsive: true,
        }">
        <template #column-6="props">
            <div class="flex gap-2">

                <UIButton @click="openClick(props.rowData)">
                    Открыть
                </UIButton>
            </div>
            
        </template>
    </DataTable>
    

</template>
<script setup>
import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net';
import { onMounted, ref } from 'vue'
import axios from 'axios'
import 'datatables.net-select';
import 'datatables.net-responsive';

DataTable.use(DataTablesCore);
const isOpenConfirm = ref(false)
const emit = defineEmits(['dt-ready']);
let dt
const table = ref()
const selectedRowId = ref();
const selectedRow = ref()
const dataTableVisible = ref(true)
const router = useRouter();
onMounted(function () {
    dt = table.value.dt;
    emit('dt-ready', dt);
});
const columns = [
    { data: 'name', title: 'Имя' },
    { data: 'family_name', title: 'Фамилия' },
    { data: 'second_name', title: 'Отчество' },
    { data: 'email', title: 'E-Mail' },
    { data: 'phone', title: 'Телефон' },
    { data: 'id', title: 'ID' },
    { title: 'Действия', data: null, defaultContent: '', orderable: false, searchable: false, className: 'dt-center' }

]

function openClick(data) {
    console.log(data.id)
    router.push(`/staffs/${data.id}`)

}

function reloadTable() {
    dataTableVisible.value = false;
    nextTick(() => {
        dataTableVisible.value = true;
    });
    dt.ajax.reload()
}
defineExpose({
    reloadTable
})

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