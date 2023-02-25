/*function copyText(htmlElement){
  if(!htmlElement){
    return;
  }
  //let elementText = htmlElement.innerText;
  let inputElement = document.createElement('a');
  inputElement.setAttribute('id',"short-url");
  document.body.appendChild(inputElement);
  inputElement.select();
  document.execcommand('copy');
  inputElement.parentNode.removeChild(inputElement);

  
}


document.querySelector('#copy-url').onclick = 
function(){
  copyText(document.querySelector("#short-url"));
}*/
/*

const token = document.querySelector("a");

token.addEventListener("click", async (event) => {
  if (!navigator.clipboard) {
    return;
  }  
  
  try {
    const text = event.target.innerText;
    await navigator.clipboard.writeText(text);
    
    event.target.dataset.clipboard = text;
    setTimeout(() =>{
      delete event.target.dataset.clipboard;
    }, 1500);    
  } catch (error) {
    console.error("Copy failed", error);
  }
});*/

let text = document.getElementById('short-url').innerHTML;
  const copyContent = async () => {
    try {
      await navigator.clipboard.writeText(text);
      console.log('Content copied to clipboard');
    } catch (err) {
      console.error('Failed to copy: ', err);
    }
  }
  