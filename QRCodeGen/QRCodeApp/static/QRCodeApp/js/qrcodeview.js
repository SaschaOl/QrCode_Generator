const popupList = document.querySelectorAll(".popup")
const detailsList = document.querySelectorAll(".details")

for (let i = 0; i < detailsList.length; i++){
    let popup 
    for (let a = 0; a < popupList.length; a++){
        console.log(popupList[a].id == detailsList[i].id)
        console.log(a)
        console.log(popupList[a].id)
        console.log(detailsList[i].id)
        if (popupList[a].id == detailsList[i].id){
            popup = popupList[a];
            break
        }
    }
    detailsList[i].addEventListener(
        "click", () =>{
            popup.classList.toggle("show");
            popup.classList.toggle("hide");
            
        }
    ) 

    popup.addEventListener(
        "click",
        () => {
            popup.classList.toggle("show");
            popup.classList.toggle("hide");
        }
    )
}




