<template>
  <div class="grid grid-cols-[1fr,6fr]">
    <Sidebar />
    <div class="max-md:p-4 p-6">
      <slot />
      <UNotifications />

    </div>
  </div>
</template>