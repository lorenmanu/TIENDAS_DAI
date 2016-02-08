<script type="text/javascript" src="js/highcharts1/highcharts-2.3.5.js"></script>
<script type="text/javascript" src="js/highcharts1/modules/exporting-2.3.5.js"></script>
function Visualiza_datos(datos){
        $('#container').highcharts({
            chart: { type: 'bar', animation:'true' },
            title: { text: 'Visitas de las tiendas' },
            xAxis: { categories: datos[0] },
            //xAxis: {categories: ["Almendro", "mariapilar bar", "Ecu", "Conchita", "Entre ascuas", "Casa Blanca"]},
            yAxis: {
                title:{
                    text:'Visitas'
                }
            },
            series: [{
                data: datos[1],
                name:"numero de visitas",
                //data : [74, 20, 9, 6, 3, 2]
            }],
        });
    };