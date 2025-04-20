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
        /* position: fixed;
        top: 0; */
        position: relative;
        margin: auto;
        width: 90% !important;
        padding: 2rem 2rem 0 2rem !important;
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: transparent;
        border-bottom: 1px solid #b09e80;
        overflow-x: hidden;
    }

    .logo {
        width: auto;
        height: 80px;
    }
</style>