var map = L.map('map').setView([-6.92154, 107.61102], 13);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    $.ajax({
        "url": `${location.protocol}//${location.hostname}/ajax/lokasi`,
        "type": "POST",
        success: function(result) {
            $.each(result, function(key, data) {
                const marker = L.marker([data.lat_lokasi, data.lon_lokasi]).bindTooltip(data.nama_lokasi, {
                    direction: 'top'
                }).addTo(map)
                marker.on('click', function() {
                    showListCamera(data.id_lokasi)
                });
            });
        },
        error: function() {
            alert('Gagal mengambil data peta')
        }
    });