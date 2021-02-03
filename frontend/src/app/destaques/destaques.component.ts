import { Component, OnInit } from '@angular/core'
import { environment } from '../../environments/environment'
import get from 'axios'

@Component({
  selector: 'app-destaques',
  templateUrl: './destaques.component.html',
  styleUrls: ['./destaques.component.scss'],
})
export class DestaquesComponent implements OnInit {
  private API_URL = environment.API_URL
  destaques: Array<Object>
  constructor() {}

  ngOnInit(): void {
    get(`${this.API_URL}produtos`).then((response) => {
      this.destaques = response.data
      console.log(this.destaques)
    })
  }
}
