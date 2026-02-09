function confirmar(urlDestino, texto) {
    console.log("fue llamada");
    Swal.fire({
        title: '¿Está seguro?',
        text: "Esta acción no se puede deshacer",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sí',
        cancelButtonText: 'No',
        width: '300px',
        hight: '300px',
        customClass: {
            popup: 'popup-pequeno'
        }
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire(texto)
            window.location.href = urlDestino;
        } else {
            Swal.fire('acción cancelada');
        }
    });
}

function showMessage(message, time) {
    console.log("el mensaje es recibido")
    const box = document.createElement("div");
    box.className = "custom-message-box";
    box.textContent = message;
    document.body.appendChild(box);
    setTimeout(() => { box.remove(); }, time*1000);
}