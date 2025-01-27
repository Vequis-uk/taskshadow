    document.addEventListener('DOMContentLoaded', () => {
    const messages = document.querySelectorAll('.message');
    setTimeout(() => {
    messages.forEach(message => message.remove());
}, 3000); // 3 seconds
});
