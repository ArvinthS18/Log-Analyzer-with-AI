// // // import { Component } from '@angular/core';
// // // import { HttpClient, HttpErrorResponse } from '@angular/common/http';

// // // interface LogEntry {
// // //   [key: string]: string;
// // // }

// // // @Component({
// // //   selector: 'app-root',
// // //   templateUrl: './app.component.html',
// // //   styleUrls: ['./app.component.css']
// // // })
// // // export class AppComponent {
// // //   selectedFile: File | null = null;
// // //   header: string[] = [];
// // //   tableData: LogEntry[] = [];
// // //   displayedTableData: LogEntry[] = [];
// // //   error: string | null = null;
// // //   isLoading: boolean = false;
// // //   pageSize: number = 10;
// // //   currentPage: number = 1;
// // //   totalPages: number = 0;
// // //   pages: number[] = [];

// // //   constructor(private http: HttpClient) {}

// // //   onFileSelected(event: any) {
// // //     this.selectedFile = event.target.files[0];
// // //   }

// // //   analyzeFile() {
// // //     if (!this.selectedFile) {
// // //       this.error = 'No file selected!';
// // //       return;
// // //     }

// // //     this.isLoading = true;
// // //     this.error = null;

// // //     const formData = new FormData();
// // //     formData.append('file', this.selectedFile);

// // //     this.http.post<any>('http://127.0.0.1:5000/api/analyze', formData)
// // //       .subscribe(response => {
// // //         this.isLoading = false;
// // //         console.log('Response:', response);
// // //         if (response && response.error) {
// // //           this.error = response.error;
// // //           this.header = [];
// // //           this.tableData = [];
// // //         } else {
// // //           this.error = null;
// // //           this.header = Object.keys(response.logs[0]) || [];
// // //           this.tableData = response.logs || [];
// // //           this.totalPages = Math.ceil(this.tableData.length / this.pageSize);
// // //           this.pages = Array.from({ length: this.totalPages }, (_, i) => i + 1);
// // //           this.setDisplayedTableData();
// // //         }
// // //       },
// // //       (error: HttpErrorResponse) => {
// // //         this.isLoading = false;
// // //         let errorMessage = `Error analyzing file: ${error.message}`;
// // //         console.error(errorMessage);
// // //         this.error = errorMessage;
// // //       });
// // //   }

// // //   onPageChange(pageNumber: number) {
// // //     this.currentPage = pageNumber;
// // //     this.setDisplayedTableData();
// // //   }

// // //   setDisplayedTableData() {
// // //     const startIndex = (this.currentPage - 1) * this.pageSize;
// // //     const endIndex = Math.min(startIndex + this.pageSize, this.tableData.length);
// // //     this.displayedTableData = this.tableData.slice(startIndex, endIndex);
// // //   }

// // //   getObjectKeys(obj: Object): string[] {
// // //     return Object.keys(obj);
// // //   }
// // // }
// // import { Component } from '@angular/core';
// // import { HttpClient, HttpErrorResponse } from '@angular/common/http';

// // interface LogEntry {
// //   [key: string]: string;
// // }

// // @Component({
// //   selector: 'app-root',
// //   templateUrl: './app.component.html',
// //   styleUrls: ['./app.component.css']
// // })
// // export class AppComponent {
// //   selectedFile: File | null = null;
// //   promptValue: string = ''; // Added promptValue variable
// //   header: string[] = [];
// //   tableData: LogEntry[] = [];
// //   displayedTableData: LogEntry[] = [];
// //   error: string | null = null;
// //   isLoading: boolean = false;
// //   pageSize: number = 10;
// //   currentPage: number = 1;
// //   totalPages: number = 0;
// //   pages: number[] = [];

// //   constructor(private http: HttpClient) {}

// //   onFileSelected(event: any) {
// //     this.selectedFile = event.target.files[0];
// //   }

// //   analyzeFile() {
// //     if (!this.selectedFile) {
// //       this.error = 'No file selected!';
// //       return;
// //     }

// //     this.isLoading = true;
// //     this.error = null;

// //     const formData = new FormData();
// //     formData.append('file', this.selectedFile);
// //     formData.append('prompt', this.promptValue); // Include prompt in the formData

// //     this.http.post<any>('http://127.0.0.1:5000/api/analyze', formData)
// //       .subscribe(response => {
// //         this.isLoading = false;
// //         console.log('Response:', response);
// //         if (response && response.error) {
// //           this.error = response.error;
// //           this.header = [];
// //           this.tableData = [];
// //         } else {
// //           this.error = null;
// //           this.header = Object.keys(response.logs[0]) || [];
// //           this.tableData = response.logs || [];
// //           this.totalPages = Math.ceil(this.tableData.length / this.pageSize);
// //           this.pages = Array.from({ length: this.totalPages }, (_, i) => i + 1);
// //           this.setDisplayedTableData();
// //         }
// //       },
// //       (error: HttpErrorResponse) => {
// //         this.isLoading = false;
// //         let errorMessage = `Error analyzing file: ${error.message}`;
// //         console.error(errorMessage);
// //         this.error = errorMessage;
// //       });
// //   }

// //   onPageChange(pageNumber: number) {
// //     this.currentPage = pageNumber;
// //     this.setDisplayedTableData();
// //   }

// //   setDisplayedTableData() {
// //     const startIndex = (this.currentPage - 1) * this.pageSize;
// //     const endIndex = Math.min(startIndex + this.pageSize, this.tableData.length);
// //     this.displayedTableData = this.tableData.slice(startIndex, endIndex);
// //   }

// //   getObjectKeys(obj: Object): string[] {
// //     return Object.keys(obj);
// //   }
// // }
// import { Component } from '@angular/core';
// import { HttpClient, HttpErrorResponse } from '@angular/common/http';

// interface LogEntry {
//   [key: string]: string;
// }

// @Component({
//   selector: 'app-root',
//   templateUrl: './app.component.html',
//   styleUrls: ['./app.component.css']
// })
// export class AppComponent {
//   selectedFile: File | null = null;
//   promptValue: string = '';
//   header: string[] = [];
//   tableData: LogEntry[] = [];
//   displayedTableData: LogEntry[] = [];
//   error: string | null = null;
//   isLoading: boolean = false;
//   analysisData: string | null = null;
//   pageSize: number = 10;
//   currentPage: number = 1;
//   totalPages: number = 0;
//   pages: number[] = [];

//   constructor(private http: HttpClient) {}

//   onFileSelected(event: any) {
//     this.selectedFile = event.target.files[0];
//   }

//   analyzeFile() {
//     if (!this.selectedFile) {
//       this.error = 'No file selected!';
//       return;
//     }

//     this.isLoading = true;
//     this.error = null;

//     const formData = new FormData();
//     formData.append('file', this.selectedFile);
//     formData.append('prompt', this.promptValue);

//     this.http.post<any>('http://127.0.0.1:5000/api/analyze', formData)
//       .subscribe(response => {
//         this.isLoading = false;
//         console.log('Response:', response);
//         if (response && response.error) {
//           this.error = response.error;
//           this.analysisData = null;
//         } else {
//           this.error = null;
//           this.analysisData = response.analysis_data || null;
//         }
//       },
//       (error: HttpErrorResponse) => {
//         this.isLoading = false;
//         let errorMessage = `Error analyzing file: ${error.message}`;
//         console.error(errorMessage);
//         this.error = errorMessage;
//         this.analysisData = null;
//       });
//   }

//   onPageChange(pageNumber: number) {
//     this.currentPage = pageNumber;
//     this.setDisplayedTableData();
//   }

//   setDisplayedTableData() {
//     const startIndex = (this.currentPage - 1) * this.pageSize;
//     const endIndex = Math.min(startIndex + this.pageSize, this.tableData.length);
//     this.displayedTableData = this.tableData.slice(startIndex, endIndex);
//   }

//   getObjectKeys(obj: Object): string[] {
//     return Object.keys(obj);
//   }
// }
import { Component } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  selectedFile: File | null = null;
  promptValue: string = '';
  error: string | null = null;
  isLoading: boolean = false;
  timestamps: string[] = [];
  messages: string[] = [];
  response_texts: string[] = [];

  constructor(private http: HttpClient) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  analyzeFile() {
    if (!this.selectedFile) {
      this.error = 'No file selected!';
      return;
    }

    this.isLoading = true;
    this.error = null;

    const formData = new FormData();
    formData.append('file', this.selectedFile);
    formData.append('prompt', this.promptValue);

    this.http.post<any>('http://127.0.0.1:5000/api/analyze', formData)
      .subscribe(response => {
        this.isLoading = false;
        console.log('Response:', response);
        if (response && response.error) {
          this.error = response.error;
        } else {
          this.error = null;
          this.timestamps = response.timestamps || [];
          this.messages = response.messages || [];
          this.response_texts = response.response_texts || [];
        }
      },
      (error: HttpErrorResponse) => {
        this.isLoading = false;
        let errorMessage = `Error analyzing file: ${error.message}`;
        console.error(errorMessage);
        this.error = errorMessage;
        this.timestamps = [];
        this.messages = [];
        this.response_texts = [];
        console.log(this.response_texts)
      });
  }
}
