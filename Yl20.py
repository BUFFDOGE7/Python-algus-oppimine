def calculate_upc_checksum(upc_code):
    """
    Calculate the checksum digit for a UPC barcode.
    
    Args:
        upc_code: String or integer representing the first 11 digits of UPC
        
    Returns:
        Integer representing the checksum digit (0-9)
    """
    upc_str = str(upc_code).zfill(11)
    
    if len(upc_str) != 11:
        raise ValueError("UPC code must be 11 digits")
    
    odd_sum = sum(int(upc_str[i]) for i in range(0, 11, 2))
    
    even_sum = sum(int(upc_str[i]) for i in range(1, 11, 2))
    
    total = (odd_sum * 3) + even_sum
    
    remainder = total % 10
    checksum = (10 - remainder) % 10
    
    return checksum


def verify_upc(upc_code):
    """
    Verify if a 12-digit UPC code is valid.
    
    Args:
        upc_code: String or integer representing the full 12-digit UPC
        
    Returns:
        Boolean indicating if the UPC is valid
    """
    upc_str = str(upc_code).zfill(12)
    
    if len(upc_str) != 12:
        return False
    
    calculated_checksum = calculate_upc_checksum(upc_str[:11])
    
    return calculated_checksum == int(upc_str[11])

if __name__ == "__main__":
    test_upc = "03600029145"
    checksum = calculate_upc_checksum(test_upc)
    print(f"UPC: {test_upc}")
    print(f"Checksum digit: {checksum}")
    print(f"Full UPC: {test_upc}{checksum}")
    print()
    
    valid_upc = "036000291452"
    invalid_upc = "036000291453"
    
    print(f"Verifying {valid_upc}: {verify_upc(valid_upc)}")
    print(f"Verifying {invalid_upc}: {verify_upc(invalid_upc)}")
    print()
    
    test_cases = [
        "01234567890",
        "78914801234",
    ]
    
    for upc in test_cases:
        cs = calculate_upc_checksum(upc)
        print(f"{upc} → Checksum: {cs} → Full UPC: {upc}{cs}")