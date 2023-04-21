from fpdf import FPDF

def calc():

  income = int((input("To get started, enter your yearly income: $").replace(',', '')))
  writeoffs = int((input("Enter your write-off: $").replace(',', '')))  #Savings
  state = input("Enter your state (Two-letter abbreviation UPPERCASE): ")
  print("\n1. Single Filer\n2. Married Filing jointly\n3. Married Filing separately")
  status = int(input("From the options above, which one are you: "))

  if status == 1:
    pass
  elif status == 2:
    income = income - 25900  # Standard Deduction
    sd = "$25,900"
  elif status == 3:
    income = income - 12950  # Standard Deduction
  else:
    print("Invalid input")
    quit()

  if state == 'PA':
    tax = 0.0857  # 8.57%
  elif state == 'NY':
    tax = 0.1275
  elif state == 'HI':
    tax = 0.1270
  elif state == 'ME':
    tax = 0.1142
  elif state == 'VT':
    tax = 0.1113
  elif state == 'MN':
    tax = 0.1020
  elif state == 'NJ':
    tax = 0.1011
  elif state == 'CT':
    tax = 0.1006
  elif state == 'RI':
    tax = 0.0991
  elif state == 'CA':
    tax = 0.0974
  elif state == 'IL':
    tax = 0.0970
  elif state == 'MD':
    tax = 0.0947
  elif state == 'NM':
    tax = 0.0937
  elif state == 'IA':
    tax = 0.0934
  elif state == 'KS':
    tax = 0.0934
  elif state == 'UT':
    tax = 0.0913
  elif state == 'MS':
    tax = 0.0916
  elif state == 'WV':
    tax = 0.0908
  elif state == 'NE':
    tax = 0.0901
  elif state == 'OH':
    tax = 0.0899
  elif state == 'WI':
    tax = 0.0892
  elif state == 'MA':
    tax = 0.0880
  elif state == 'AK':
    tax = 0.0877
  elif state == 'KY':
    tax = 0.0877
  elif state == 'LA':
    tax = 0.0875
  elif state == 'OR':
    tax = 0.0865
  elif state == 'CO':
    tax = 0.0852
  elif state == 'IN':
    tax = 0.0842
  elif state == 'AZ':
    tax = 0.0839
  elif state == 'WA':
    tax = 0.0837
  elif state == 'MI':
    tax = 0.0825
  elif state == 'TX':
    tax = 0.0822
  elif state == 'NV':
    tax = 0.0819
  elif state == 'VA':
    tax = 0.0819
  elif state == 'NC':
    tax = 0.0816
  elif state == 'GA':
    tax = 0.0801
  elif state == 'ND':
    tax = 0.0800
  elif state == 'MO':
    tax = 0.0780
  elif state == 'SC':
    tax = 0.0767
  elif state == 'ID':
    tax = 0.0759
  elif state == 'OK':
    tax = 0.0747
  elif state == 'AL':
    tax = 0.0741
  elif state == 'MT':
    tax = 0.0739
  elif state == 'SD':
    tax = 0.0712
  elif state == 'FL':
    tax = 0.0664
  elif state == 'NH':
    tax = 0.0641
  elif state == 'WY':
    tax = 0.0632
  elif state == 'DE':
    tax = 0.0622
  elif state == 'TN':
    tax = 0.0575
  elif state == 'AK':
    tax = 0.0506

  else:
    print("Sorry, your input is not recognized. Please enter a valid UPPERCASE state abbreviation.")
    quit()

  result = str((income - writeoffs) * tax)
  print("\nYour amount to pay: $" + result)

  bd = input("Would you like to download your full breakdown (y/n): ")


  #PDF
  if (bd == 'y' or bd == 'Y'):

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, 'TaxCalc report', 1, 1, 'C')
    pdf.set_font('Arial', '', 12)
    pdf.ln()
    pdf.cell(w=0, h=10, txt=f"Your Income: ${income}", ln=1, align='L')
    pdf.cell(w=0, h=10, txt=f"State: {state}", ln=1, align='L')
    pdf.cell(w=0, h=10, txt=f"Tax Rate: {tax*100}%", ln=1, align='L')
    pdf.cell(w=0, h=10, txt=f"Write-off: ${writeoffs}", ln=1, align='L')
    pdf.cell(w=0, h=10, txt=f"Amount to Pay: ${result}", ln=1, align='L')

    if status == 1:
      pdf.cell(w=0, h=10, txt="Marital Status: Single", ln=1, align='L')
      pdf.cell(w=0, h=10, txt="Standard Deduction: NA", ln=1, align='L')
    elif status == 2:
      pdf.cell(w=0, h=10, txt="Marital Status: Married Filing jointly", ln=1, align='L')
      pdf.cell(w=0, h=10, txt="Standard Deduction: $25,900", ln=1, align='L')
    elif status == 3:
      pdf.cell(w=0, h=10, txt="Marital Status: Married Filing jointly", ln=1, align='L')
      pdf.cell(w=0, h=10, txt="Standard Deduction: $12,950", ln=1, align='L')
    pdf.cell(w=0, h=10, txt="", ln=1, align='L')
    pdf.cell(w=0, h=10, txt="", ln=1, align='L')
    pdf.cell(w=0, h=10, txt="", ln=1, align='L')

    pdf.set_font('Arial', 'I', 10)
    pdf.cell(w=0, h=10, txt="Joint filers usually receive higher income thresholds for certain tax breaks, such as the deduction for contributing to an IRA", ln=1)

    pdf.output(f'./taxinfo.pdf', 'F')
    print("\nDownloaded successfully!")

  elif (bd == 'n' or bd == 'N'):
    quit()

if __name__ == "__main__":
  print("\n\n*************************************************************")
  print("| ████████╗░█████╗░██╗░░██╗░█████╗░░█████╗░██╗░░░░░░█████╗░ |")
  print("| ╚══██╔══╝██╔══██╗╚██╗██╔╝██╔══██╗██╔══██╗██║░░░░░██╔══██╗ |")
  print("| ░░░██║░░░███████║░╚███╔╝░██║░░╚═╝███████║██║░░░░░██║░░╚═╝ |")
  print("| ░░░██║░░░██╔══██║░██╔██╗░██║░░██╗██╔══██║██║░░░░░██║░░██╗ |")
  print("| ░░░██║░░░██║░░██║██╔╝╚██╗╚█████╔╝██║░░██║███████╗╚█████╔╝ |")
  print("| ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░ |")
  print("*************************************************************\n")
  calc()
