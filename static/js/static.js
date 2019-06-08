L.mapquest.key = '652SIqyYTPdWXYRRyJ9T9yrXnjd4dzPG';

// 'map' refers to a <div> element with the ID map


var map = L.mapquest.map('map1', {
  center: [43.6532, -79.3832],
  layers: L.mapquest.tileLayer('map'),
  zoom: 15
});

//var lArray = ["570 Bay st, Toronto", "37 charles st e,Toronto", "1001 Bay st, Toronto","75 queen st w, Toronto","777 bay st","20 spadina ave, Toronto","1 yonge, toronto"]

var url = "http://www.mapquestapi.com/geocoding/v1/address?key=KEY";
submit.on("click", function() {
    d3.json(url, function(response) {
    
    var inputElement_date = d3.select("#date");
    var inputElement_time = d3.select("#time");
    var inputElement_location = d3.select("#location");
    var inputElement_fine_type = d3.select("#fine_type");

   // var inputValue_date = inputElement_date.property("value");
    var inputValue_time = inputElement_time.property("value");
//var inputValue_location = inputElement_location.property("value");
    var inputValue_fine_type = inputElement_fine_type.property("value");
    
   // var filteredData = response;
//  console.log(response);

var lArray = {};
var location =[];
var location_count = [];
var total_location_count = 0;
var fine_count = [];
var fine_type = [];
var total_fines = 0;
var time = ["0-1","1-2","2-3","3-4","4-5","5-6","6-7","7-8","8-9","9-10","10-11","11-12","12-13","13-14","14-15","15-16","16-17","17-18","18-19","19-20","20-21","21-22","22-23","23-24"];
var time_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];

for (var i = 0; i < response.length; i++) {
    if (location.includes(response[i].location2)){
        location_count[location.indexOf(response[i].location2)]=location_count[location.indexOf(response[i].location2)]+1;
        
        }
    else{
        location.push(response[i].location2);
        location_count.push(1);
        };

    if (fine_type.includes(response[i].infraction_description)){
            fine_count[fine_type.indexOf(response[i].infraction_description)]=fine_count[fine_type.indexOf(response[i].infraction_description)]+1;
            
        }
    else{
        fine_type.push(response[i].infraction_description);
        fine_count.push(1);
        } ;
    if ((response[i].time_of_infraction>=2300)){
        time_count[23]=time_count[23]+1;
        }
    else if((response[i].time_of_infraction>=2200)){
        time_count[22]=time_count[22]+1;
        }
    else if((response[i].time_of_infraction>=2100)){
        time_count[21]=time_count[21]+1;
        }
    else if((response[i].time_of_infraction>=2100)){
        time_count[21]=time_count[21]+1;
        }
    else if((response[i].time_of_infraction>=2000)){
        time_count[20]=time_count[20]+1;
        }
    else if((response[i].time_of_infraction>=1900)){
        time_count[19]=time_count[19]+1;
        }
    else if((response[i].time_of_infraction>=1800)){
        time_count[18]=time_count[18]+1;
        }
    else if((response[i].time_of_infraction>=1700)){
        time_count[17]=time_count[17]+1;
        }
    else if((response[i].time_of_infraction>=1600)){
        time_count[16]=time_count[16]+1;
        }
    else if((response[i].time_of_infraction>=1500)){
        time_count[15]=time_count[15]+1;
        }
    else if((response[i].time_of_infraction>=1400)){
        time_count[14]=time_count[14]+1;
        }
    else if((response[i].time_of_infraction>=1300)){
        time_count[13]=time_count[13]+1;
    }
    else if((response[i].time_of_infraction>=1200)){
        time_count[12]=time_count[12]+1;
        }
    else if((response[i].time_of_infraction>=1100)){
        time_count[11]=time_count[11]+1;
        }
    else if((response[i].time_of_infraction>=1000)){
        time_count[10]=time_count[10]+1;
        }
    else if((response[i].time_of_infraction>=900)){
        time_count[9]=time_count[9]+1;
        }
    else if((response[i].time_of_infraction>=800)){
        time_count[8]=time_count[8]+1;
        }
    else if((response[i].time_of_infraction>=700)){
        time_count[7]=time_count[7]+1;
        }
    else if((response[i].time_of_infraction>=600)){
        time_count[6]=time_count[6]+1;
        }
    else if((response[i].time_of_infraction>=500)){
        time_count[5]=time_count[5]+1;
        }
    else if((response[i].time_of_infraction>=400)){
        time_count[4]=time_count[4]+1;
        }
    else if((response[i].time_of_infraction>=300)){
        time_count[3]=time_count[3]+1;
        }
    else if((response[i].time_of_infraction>=200)){
        time_count[2]=time_count[2]+1;
        }
    else if((response[i].time_of_infraction>=100)){
        time_count[1]=time_count[1]+1;
        }
    else{
        time_count[0]=time_count[0]+1;
    }
    }

  lArray.push(location,);
  L.mapquest.geocoding().geocode(lArray);

//pie chart building
  var trace1 = {
    labels: location,
    values: location_count,
    text: location,
    type: 'pie'
     };
    
    var data1 = [trace1];
    
    var layout = {
    title: "'Fine Type Proportion",
    };
    
   Plotly.newPlot("piechart1", data1, layout);

   var trace2 = {
    labels: fine_type,
    values: fine_count,
    text: fine_type,
    type: 'pie'
     };
    
    var data2 = [trace2];
    
    var layout = {
    title: "Fine Type Proportion",
    };
    
   Plotly.newPlot("piechart2", data2, layout);

   var trace3 = {
    labels: time,
    values: time_count,
    text: time,
    type: 'pie'
     };
    
    var data3 = [trace3];
    
    var layout = {
    title: "Fine Time Proportion",
    };
    
   Plotly.newPlot("piechart3", data3, layout);

});
});


 