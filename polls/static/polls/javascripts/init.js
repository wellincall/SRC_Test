
function addCaption(paramData){
	for(index in paramData){
		var newRow = document.createElement("TR");
		var captionContainer = document.createElement("TD");
		var color = document.createElement("TD");
		color.setAttribute("bgcolor", paramData[index].color);
		var captionText = document.createTextNode(paramData[index].caption);
		captionContainer.appendChild(captionText);
		newRow.appendChild(color);
		newRow.appendChild(captionContainer);
		document.querySelectorAll('[class="caption_description"]')[0].appendChild(newRow);
	}
}
