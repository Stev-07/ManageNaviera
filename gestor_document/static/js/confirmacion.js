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

