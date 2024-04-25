
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
