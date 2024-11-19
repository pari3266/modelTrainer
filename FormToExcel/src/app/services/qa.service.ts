import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class QaService {
  private apiUrl = 'http://127.0.0.1:8000/predict'; // آدرس سرور FastAPI

  constructor(private http: HttpClient) {}

  getAnswer(question: string): Observable<{ answer: string }> {
    return this.http.post<{ answer: string }>(this.apiUrl, { question });
  }
}
