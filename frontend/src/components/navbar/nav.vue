<script>
import navModal from './navModal.vue'
// import logo from '@/assets/Gotel-logo-fedbbdcb.jpg'

</script>

<template>
    <nav class="w-100">
        <div>
            <img  src="../../assets/Gotel-logo-fedbbdcb.jpg" alt="Gotel" class="logo"/>
        </div>
        <NavModal></NavModal>   
    </nav>
</template>

<style scoped>
    nav {
        position: fixed;
        top: 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background: transparent;
    }

    .logo {
        width: auto;
        height: 80px;
    }
</style>