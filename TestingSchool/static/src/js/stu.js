
var loadFile = function(event){
var image = document.getElementById('output');
if(event.target.files.length > 0) {
image.src = URL.createObjectURL(event.target.files[0]);
}
};

function CF(){
$('#file').click()
}

function namecombiod1()
{
var fullPath = document.getElementById('attachment').value;
var image = document.getElementById('attachment');
if(event.target.files.length > 0){
image.src = URL.createObjectURL(event.target.files[0]);
document.getElementById('document1').src = image.src;
}
if (fullPath){
var startIndex = (fullPath.indexOf('\\') > 0 ? fullPath.lastIndexOf('\\'): fullPath.lastIndexOf('/'));
var filename = fullPath.substring(startIndex);
if(filename.indexOf('\\')=== 0 || filename.indexOf('/')=== 0 ){
filename = filename.substring(1);
var name = filename.substr(0, filename.lastIndexOf('.'));
var extension = filename.split('.').pop();
}
if((extension == 'jpg') || (extension =='png')){
$('#show_attachment').html(name+'.'+extension);
document.getElementById('pdfpath1').style.display = 'none';
document.getElementById('show_attachment').style.display = 'block';
}

if(extension == 'pdf'){
$('#pdf_name1').html(name+'.'+extension);
document.getElementById('pdfpath1').href = image.src;
document.getElementById('pdfpath1').style.display = 'block';
document.getElementById('show_attachment').style.display = 'none';
}

}
}

function show_od1_hide(){
var x= document.getElementById('hide_od1');
x.style.display='none';
}

function check_birth_date() {
    var UserDate = document.getElementById("birth_date").value;
    var ToDate = new Date();

    if (new Date(UserDate).getTime() > ToDate.getTime()) {
          alert("Birthdate must be less than today date");
          return false;
     }
    return true;
}


const source = document.getElementById('sn');
const result = document.getElementById('snr');

const inputHandler = function(e) {
  result.innerHTML = e.target.value;
}

source.addEventListener('sn', inputHandler);
source.addEventListener('snr', inputHandler); // for IE8
// Firefox/Edge18-/IE9+ don’t fire on <select><option>
// source.addEventListener('change', inputHandler);