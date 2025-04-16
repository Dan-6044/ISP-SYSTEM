document.addEventListener('DOMContentLoaded', function () {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');
    const toggleBtn = document.getElementById('toggleSidebarBtn');
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');

    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.href === window.location.href) {
            link.classList.add('active');
        }

        link.addEventListener('click', () => {
            if (window.innerWidth < 992) {
                sidebar.classList.remove('mobile-open');
                overlay.classList.remove('visible');
            }
        });
    });

    toggleBtn.addEventListener('click', () => {
        sidebar.classList.toggle('collapsed');
    });

    mobileMenuBtn.addEventListener('click', () => {
        sidebar.classList.add('mobile-open');
        overlay.classList.add('visible');
    });

    overlay.addEventListener('click', () => {
        sidebar.classList.remove('mobile-open');
        overlay.classList.remove('visible');
    });
});