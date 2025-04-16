const themeToggleButton = document.getElementById('theme-toggle');

// Получаем текущую тему из localStorage или по умолчанию "light"
let currentTheme = localStorage.getItem('theme') || 'light';
document.body.classList.add(currentTheme + '-theme');

// Устанавливаем иконку по текущей теме
themeToggleButton.textContent = currentTheme === 'dark' ? '🌞' : '🌙';

// Обработчик переключения темы
themeToggleButton.addEventListener('click', () => {
    let newTheme = document.body.classList.contains('light-theme') ? 'dark' : 'light';
    document.body.classList.remove('light-theme', 'dark-theme');
    document.body.classList.add(newTheme + '-theme');

    // Обновляем иконку
    themeToggleButton.textContent = newTheme === 'dark' ? '🌞' : '🌙';

    // Сохраняем тему
    localStorage.setItem('theme', newTheme);
});



