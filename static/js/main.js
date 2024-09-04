
  let searchform=document.getElementById('searchform')
  let pagelink=document.getElementsByClassName('page-link')

  if (searchform){
   for(let i=0;pagelink.length > i;i++){
   pagelink[i].addEventListener('click', function (e){
    e.preventDefault()
    let page=this.dataset.page
    
    searchform.innerHTML+=`<input value=${page} name="page" hidden/>`
    

    searchform.submit()
 
   })
   }
  }

