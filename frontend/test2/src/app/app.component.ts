import { Component } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

interface LogEntry {
  [key: string]: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  selectedFile: File | null = null;
  header: string[] = [];
  tableData: LogEntry[] = [];
  error: string | null = null;

  constructor(private http: HttpClient) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  analyzeFile() {
    if (!this.selectedFile) {
      this.error = 'No file selected!';
      return;
    }

    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.http.post<any>('http://127.0.0.1:5000/api/analyze', formData)
      .subscribe(response => {
        console.log('Response:', response);
        if (response && response.error) {
          this.error = response.error;
          this.header = []; // Reset header if error occurs
          this.tableData = []; // Reset table data if error occurs
        } else {
          this.error = null;
          this.header = response.header || []; // If no header, initialize as empty array
          this.tableData = response.data || []; // If no data, initialize as empty array
        }
      },
      (error: HttpErrorResponse) => {
        console.error('Error analyzing file:', error);
        this.error = 'Error analyzing file: ' + error.message;
      });
  }

  // Helper function to get object keys
  getObjectKeys(obj: Object): string[] {
    return Object.keys(obj);
  }
}
