import { Component } from '@angular/core';
import * as XLSX from 'xlsx';

@Component({
  selector: 'app-excel-form',
  templateUrl: './excel-form.component.html',
  styleUrls: ['./excel-form.component.scss']
})
export class ExcelFormComponent {
  onSubmit(formData: any) {
    // Convert form data to an array of objects
    const data = [formData];

    // Create a new worksheet
    const worksheet: XLSX.WorkSheet = XLSX.utils.json_to_sheet(data);

    // Create a new workbook and add the worksheet
    const workbook: XLSX.WorkBook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Form Data');

    // Save the workbook as an Excel file
    const excelBuffer: any = XLSX.write(workbook, { bookType: 'xlsx', type: 'array' });
    const blob: Blob = new Blob([excelBuffer], { type: 'application/octet-stream' });
    const fileName = 'FormData.xlsx';

    // Use FileSaver to download the file
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = fileName;
    link.click();
  }
}
