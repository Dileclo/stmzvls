<template>
    <div>
      <UIPageTitle title="Сотрудники"></UIPageTitle>
      <UButton @click="openFormModal">Добавить</UButton>
      <StaffModalAddStaff :isOpen="isFormModalOpen" @user-added="handleUserAdded" @update:isOpen="updateIsFormModalOpen" />
      <StaffTableStaff ref="dataTableComponent" @dt-ready="handleDtReady" />
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';

  const isFormModalOpen = ref(false);
  
  function openFormModal() {
    isFormModalOpen.value = true;
  }
  const dataTableComponent = ref();

  function handleUserAdded() {
    dataTableComponent.value.reloadTable();
  }
  
  function updateIsFormModalOpen(value: boolean) {
    isFormModalOpen.value = value;
  }
  
  const dt = ref();
  function handleDtReady(dtInstance: any) {
    dt.value = dtInstance;
  }
  </script>
  