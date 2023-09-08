import qrcode 

coding = qrcode.make("""
                     Name     : Abdo
                     Last Name: Haki
                     Age      : 23
                     Job      : Softwer Devlopper""")

coding.save("coding.png")