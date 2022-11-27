$(function(){
    const JWT = sessionStorage.getItem("JWT");
    const ENDERECO_IP = sessionStorage.getItem("ENDERECO_IP");
    
    function redirectToLogin() {
        window.location = "/login";
      }



    if (JWT){    
        __default_verification__()

        function __default_verification__(){
            $.ajax({
                url: `http://${ENDERECO_IP}:5000/user/info`,
                method: "GET",
                dataType: "json",
                contentType: "application/json",
                success: userIsAdminOrNot,
                headers: { Authorization: "Bearer " + JWT },
                error: () => {
                  alert("Error reading data, verify backend");
                },
              });

              function userIsAdminOrNot(data){
                const userIsAdmin = data.details.is_admin
         
                if (userIsAdmin){
                    var main = $(".main")
                    main.show()
                    var divOptionContainer = $("<div>").addClass("option-container")
                    var labelTable = $("<label>").attr("for","schemas").text("Choose Schema")
                    var divRowOptionAndInput = $("<div>").addClass("row-option-and-input") 
                    
                    var selectSchemas = $("<select>").attr("name","schemas").attr("id","schemas")
                    
                    var optionUser = $("<option>").val("user").text("User")
                    var optionGame = $("<option>").val("game").text("Game")
                    var optionGiftcard = $("<option>").val("giftcard").text("Giftcard")
                    var optionMedal = $("<option>").val("medal").text("Medal")
                    var optionPurchase = $("<option>").val("purchase").text("Purchase")
                    var optionScreenshot = $("<option>").val("screenshot").text("Screenshot")
                    var inputOption = $("<input>").attr("type","submit").val("List")
                    var hr = $("<hr>")
                    var divTableContainerAndInput = $("<div>").addClass("table-container-and-input")


                    selectSchemas.append(optionUser)
                    selectSchemas.append(optionGame)
                    selectSchemas.append(optionGiftcard)
                    selectSchemas.append(optionMedal)
                    selectSchemas.append(optionPurchase)
                    selectSchemas.append(optionScreenshot)

                    
                    divRowOptionAndInput.append(selectSchemas)
                    divRowOptionAndInput.append(inputOption)

                    divOptionContainer.append(labelTable)
                    divOptionContainer.append(divRowOptionAndInput)
                    divOptionContainer.append(hr)

                   
                    
                    divTableContainerAndInput.append(divOptionContainer)
                    main.append(divTableContainerAndInput)

                    inputOption.on("click",function(){
                        let currentValue = selectSchemas.val()

                        $(".nothing-to-show").remove()
                
                        
                        $.ajax({
                            url: `http://${ENDERECO_IP}:5000/${currentValue}/return_all`,
                            method: "GET",
                            dataType: "json",
                            contentType: "application/json",
                            headers: { Authorization: "Bearer " + JWT },
                            error: () => { alert("Error reading data, verify backend");},
                            success: function(data){
                                if (data.details.length > 0){
                                    var keys = Object.keys(data.details[0])
                                    var values = data.details
                                    keys = keys.filter(item=> item != "id")
                                    keys.unshift("id")

                                    var table = $("<table>")
                                    var trMain = $("<tr>").attr("id","tr-main")
                                    var divTable = $("<div>").addClass("table-container")

                                    $(".table-container").remove()
                                 

                                    for (let index in keys){
                                        var th = $("<th>").text(keys[index])
                                        trMain.append(th)
                                    }
                                    table.append(trMain)

                                    for (let indexUser in values){
                                        var tr = $("<tr>")
                                        for (let indexKey in keys){
                                            let key = keys[indexKey] 
                                          
                                            var td = $("<td>").text(values[indexUser][key])
                                            tr.append(td)
                                            table.append(tr)
                                        }
                                    }

                                    divTable.append(table)
                                    divTableContainerAndInput.append(divTable)
                                    main.append(divTableContainerAndInput)


                                }
                                else{
                                    $(".table-container").remove()
                                    var divNothingToShow = $("<div>").addClass("nothing-to-show")
                                    var divRowNothingToShow = $("<div>").addClass("nothing-to-show-row")
                                    var spanNothingToShow = $("<span>").text("NOTHING TO SHOW")
                                    var imgNothingToShow = $("<img>").attr("src","/static/img/fixed/logostrayerror.png")
                                    
                                    divRowNothingToShow.append(spanNothingToShow)
                                    divRowNothingToShow.append(imgNothingToShow)
                                    divNothingToShow.append(divRowNothingToShow)
                                    divTableContainerAndInput.append(divNothingToShow)
                                    
                                }
                            },
                          });
                       

                        
                    })
                    

                    inputOption.click()





                }
                else{
                    redirectToLogin()
                }

              }


            
        }
        







    }
    else{
        redirectToLogin()
    }

})