import { Component } from '@angular/core';
import { QaService } from '../services/qa.service';
@Component({
  selector: 'app-quest',
  templateUrl: './quest.component.html',
  styleUrls: ['./quest.component.scss']
})
export class QuestComponent {
  question: string = '';
  answer: string | null = null;

  constructor(private qaService: QaService) {}

  askQuestion(event: Event): void {
    event.preventDefault();
    this.qaService.getAnswer(this.question).subscribe(
      (response) => {
        this.answer = response.answer;
      },
      (error) => {
        console.error('Error:', error);
        this.answer = 'متأسفانه، پاسخی در دسترس نیست.';
      }
    );
  }
}
