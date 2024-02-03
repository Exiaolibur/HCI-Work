let myImage = document.querySelector("img");

let mydoc = document.querySelector("li")
mydoc.addEventListener("click", function(){alert("能和我组一辈子乐队吗");});



myImage.onclick = function(){
    let mySrc = myImage.getAttribute("src");

    if (mySrc === "images/mygo1.jpg"){
        myImage.setAttribute("src","images/mygo2.jpg");
    } 
    else {
        if (mySrc === "images/mygo2.jpg"){myImage.setAttribute("src","images/mygo3.jpg");} 
        else {myImage.setAttribute("src","images/mygo1.jpg");}
    }
};


let myButton = document.querySelector("button");
let myHeading = document.querySelector("p");

function setUserName() {
    let myName = prompt("请输入你的名字。");
    if (!myName) {
      myHeading.textContent = "Ano酱？";
    } else {
      localStorage.setItem("name", myName);
      myHeading.textContent = "要组一辈子MYGO！" + myName;
    }
  }

  myButton.onclick = function () {
    setUserName();
  };


