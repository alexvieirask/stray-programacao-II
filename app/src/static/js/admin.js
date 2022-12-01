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
                var user = data.details
                const userIsAdmin = data.details.is_admin
         
                if (userIsAdmin){
                    var main = $(".main")
                    main.show()
                    var divOptionContainer = $("<div>").addClass("option-container")
                    var labelTable = $("<label>").attr("for","schemas").text("Function List")
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

                   
                    
                    $(".table-container-and-input").append(divOptionContainer)
                  

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
                                    $(".table-container-and-input").append(divTable)
                                    main.append($(".table-container-and-input"))

                                   
                                }
                                else{
                                    $(".table-container").remove()
                                    console.log("teste")
                                    var divNothingToShow = $("<div>").addClass("nothing-to-show")
                                    var divRowNothingToShow = $("<div>").addClass("nothing-to-show-row")
                                    var spanNothingToShow = $("<span>").text("NOTHING TO SHOW")
                                    var imgNothingToShow = $("<img>").attr("src","/static/img/fixed/logostrayerror.png")
                                    
                                    divRowNothingToShow.append(spanNothingToShow)
                                    divRowNothingToShow.append(imgNothingToShow)
                                    divNothingToShow.append(divRowNothingToShow)
                                    $(".table-container-and-input").append(divNothingToShow)
                                    
                                }
                            },
                        });
                       

                        
                    })
                
                    inputOption.click()
                    

                    var divItemsDelete = $("<div>").addClass("items-delete")
                    var labelDelete = $("<label>").text("Function Delete")  
                    var inputDeleteId = $("<input>").attr("placeholder","ID").attr("type","text").attr("id","input-delete-id")

                    var selectSchemasDelete = $("<select>").attr("name","schemas").attr("id","schemas")
                    
                    var optionUserDelete = $("<option>").val("user").text("User")
                    var optionGameDelete = $("<option>").val("game").text("Game")
                    var optionGiftcardDelete = $("<option>").val("giftcard").text("Giftcard")
                    var optionMedalDelete= $("<option>").val("medal").text("Medal")
                    var optionPurchaseDelete = $("<option>").val("purchase").text("Purchase")
                    var optionScreenshotDelete = $("<option>").val("screenshot").text("Screenshot")
                    var inputOptionDelete = $("<button>").text("Delete").addClass("button-default").attr("id","button-delete")



                    selectSchemasDelete.append(optionUserDelete)
                    selectSchemasDelete.append(optionGameDelete)
                    selectSchemasDelete.append(optionGiftcardDelete)
                    selectSchemasDelete.append(optionMedalDelete)
                    selectSchemasDelete.append(optionPurchaseDelete)
                    selectSchemasDelete.append(optionScreenshotDelete)
                   


                    $(".delete-container").append(labelDelete)
                    divItemsDelete.append(selectSchemasDelete)
                    divItemsDelete.append(inputDeleteId)
                    divItemsDelete.append(inputOptionDelete)
                    $(".delete-container").append(divItemsDelete)



                    inputOptionDelete.on("click",function(){
                        let schema = selectSchemasDelete.val()
                        let idDelete = inputDeleteId.val()
                        $("#span-message-delete").remove()

                        if (user.id != idDelete){
                            $.ajax({
                                url: `http://${ENDERECO_IP}:5000/${schema}/delete/${idDelete}`,
                                method: "GET",
                                dataType: "json",
                                contentType: "application/json",
                                headers: { Authorization: "Bearer " + JWT },
                                error: function(){
                                    var spanDelete = $("<span>").addClass(`span-error`).text("Field empty or Invalid.").attr("id","span-message-delete")
                                    inputDeleteId.val("")
                                    divItemsDelete.append(spanDelete)
                                },
                                success: function(data){
                                    var spanDelete = $("<span>").addClass(`span-${data.result}`).text(data.details).attr("id","span-message-delete")
                                    divItemsDelete.append(spanDelete)
                                    if (data.result == "success"){
                                        setTimeout(()=>{
                                            spanDelete.hide()
                                        },2000)
                                    }
                
                                }
                              });
                        }
                        else{
                            var spanDelete = $("<span>").addClass(`span-error`).text("You cannot self delete.").attr("id","span-message-delete")
                            inputDeleteId.val("")
                            divItemsDelete.append(spanDelete)
                        }
                
                  
                    })

                    
                    var labelSendMoney = $("<label>").text("Function Send Money")
                    var inputIdToSendMoney = $("<input>").attr("type","text").attr("id","input-send-money-id").attr("placeholder","user id")
                    var inputValueToSendMoney = $("<input>").attr("type","text").attr("id","input-send-money-value").attr("placeholder","value")
                    var itemsSendMoney = $("<div>").addClass("items-send-money")
                    var buttonSendMoney = $("<button>").text("Send").addClass("button-default").attr("id","button-delete")
                    $(".edit-money-container").append(labelSendMoney)

                    itemsSendMoney.append(inputIdToSendMoney)
                    itemsSendMoney.append(inputValueToSendMoney)
                    itemsSendMoney.append(buttonSendMoney)
                    

                    $(".edit-money-container").append(itemsSendMoney)
                   
                    buttonSendMoney.on("click",function(){
                        $("#span-message-send-money").remove()
                        
                        $.ajax({
                            url: `http://${ENDERECO_IP}:5000/${inputIdToSendMoney.val()}/send/${inputValueToSendMoney.val()}`,
                            method: "GET",
                            dataType: "json",
                            contentType: "application/json",
                            success: function(data){
                                var spanSendMoney = $("<span>").addClass(`span-${data.result}`).text(data.details).attr("id","span-message-send-money")
                                itemsSendMoney.append(spanSendMoney)
                                if (data.result == "success"){
                                    setTimeout(()=>{
                                        spanSendMoney.hide()
                                    },2000)
                                }

                                if (user.id == inputIdToSendMoney.val()){
                                    let current_value = Number($(".username-wallet-header").text().split(" ")[1]) 
                                    $(".username-wallet-header").text(`R$ ${current_value + Number(inputValueToSendMoney.val())}`)
                                    
                                }
                                
                            },
                            headers: { Authorization: "Bearer " + JWT },
                            error: (data) => {
                                var spanSendMoney = $("<span>").addClass(`span-error`).text("Field empty or Invalid.").attr("id","span-message-send-money")
                                inputIdToSendMoney.val("")
                                inputValueToSendMoney.val("")
                                itemsSendMoney.append(spanSendMoney)
                            
                            },
                          });
        

                    })




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