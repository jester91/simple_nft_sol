pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollection is erc721 {
    uint256 public tokenCounter;
    constructor  () public ERC721("Dogtags","DGT"){
    tokenCounter =0;
    }

function CreateCollection (string memory tokenURI) public  returns(uint256){

    uint256 newItemID=tokenCounter;
    _safeMint(msg.sender,newItemID);
    _setTokenURI(newItemID,TokenURI);
    tokencounter++;
    return newitemID;
}


}




