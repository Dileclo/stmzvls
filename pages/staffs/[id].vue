<template>
  <div>
    <div class="flex items-center gap-2 mb-4">
      <UButton color="white" @click="router.push('/staff')">
        <Icon class="text-black" size="24px" name="akar-icons:chevron-left" />
      </UButton>
      <UIPageTitle title="Редактирование пользователя"></UIPageTitle>
    </div>

    <UForm @submit="add_user" class="" :schema="schema" :state="user">
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
      <div class="flex mt-4 gap-5">
        <UButton type="submit" class="">Изменить</UButton>
        <UButton class="" color="red" @click="deleteUser">Удалить</UButton>
      </div>
    </UForm>

  </div>
  <UModal v-model="isOpenConfirm">
    <div class="p-5 flex flex-col">
      <span>Вы уверены, что хотите удалить?</span>
      <div class="flex justify-between mt-5">
        <UButton class="px-5" color="red" @click="confirmDelete">Да</UButton>
        <UButton class="px-5" @click="isOpenConfirm = false">Нет</UButton>
      </div>
    </div>
  </UModal>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const route = useRoute();
const toast = useToast();
const isOpenConfirm = ref(false)
const user = ref({
  name: '',
  family_name: '',
  second_name: '',
  email: '',
  phone: ''
});

onMounted(() => {
  fetchUser();
});

async function fetchUser() {
  const id = route.params.id;
  try {
    const response = await axios.get(`http://127.0.0.1:8000/get_user/${id}`);
    user.value = response.data;
    console.log(user.value);
  } catch (error) {
    console.error("Ошибка при загрузке данных пользователя:", error);
  }
}

async function submitForm() {
  const id = route.params.id;
  try {
    await axios.post(`http://127.0.0.1:8000/update_user/${id}`, user.value);
    router.push('/'); // Возвращаемся на главную страницу после успешного обновления
  } catch (error) {
    console.error("Ошибка при обновлении данных пользователя:", error);
  }
}

async function deleteUser() {
  isOpenConfirm.value = true;
}

function confirmDelete() {
  const id = route.params.id;
  axios.post("http://127.0.0.1:8000/delete_user", { id: id, }).then(function (r) {
    isOpenConfirm.value = false;
    toast.add({ title: "Пользователь успешно удален" })
    router.push("/staff")
  })
}
</script>