<template>
    <UModal :modelValue="isOpen" @update:modelValue="updateIsOpen">
      <span class="p-5 text-xl">Добавить сотрудника</span>
      <UIDivider></UIDivider>
      <UForm @submit="add_user" class="p-5" :schema="schema" :state="user">
        <UFormGroup label="Фамилия" name="family_name">
          <UInput v-model="user.family_name" />
        </UFormGroup>
        <UFormGroup label="Имя" name="name">
          <UInput v-model="user.name" />
        </UFormGroup>
        <UFormGroup label="Отчество" name="second_name">
          <UInput v-model="user.second_name" />
        </UFormGroup>
        <UFormGroup label="E-Mail" name="email">
          <UInput v-model="user.email" />
        </UFormGroup>
        <UFormGroup label="Телефон" name="phone">
          <UInput v-model="user.phone" />
        </UFormGroup>
        <UFormGroup label="Должность" name="position">
          <UInput v-model="user.position" />
        </UFormGroup>
        <UButton type="submit" class="mt-4">Добавить</UButton>
      </UForm>
    </UModal>
  </template>
  
  <script setup lang="ts">
  import type { FormSubmitEvent } from '#ui/types';
  import * as Yup from 'yup';
  import axios from 'axios';
  const toast = useToast();
  
  const props = defineProps({
    isOpen: {
      type: Boolean,
      required: true
    }
  });
  
  const emit = defineEmits(['user-added', 'update:isOpen']);
  
  const schema = Yup.object({
    name: Yup.string().required('Не заполнено'),
    family_name: Yup.string().required('Не заполнено'),
    second_name: Yup.string(),
    phone: Yup.number(),
    email: Yup.string().email('Введен некоректный email').required('Не заполнено')
  });
  type Schema = Yup.InferType<typeof schema>;
  
  const user = reactive({
    name: '',
    family_name: '',
    second_name: '',
    email: '',
    phone: '',
    position: '',
    id:''
  });
  
  function add_user(event: FormSubmitEvent<Schema>) {
    axios.post('http://127.0.0.1:8000/add_user', user)
      .then(function (res) {
        toast.add({ title: 'Успешно добавлено' });
        emit('update:isOpen', false); // Закрываем модальное окно
        emit('user-added'); // Сообщаем родителю об успешном добавлении пользователя
      })
      .catch(function (err) {
        console.log(err);
        toast.add({ title: err.response.data.detail, color: 'red' });
      });
  }
  
  function updateIsOpen(value: boolean) {
    emit('update:isOpen', value);
  }
  </script>
  