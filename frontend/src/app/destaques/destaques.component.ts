import { Component, OnInit } from '@angular/core'
import { environment } from '../../environments/environment'
import { NgbCarouselConfig } from '@ng-bootstrap/ng-bootstrap'
import get from 'axios'

@Component({
  selector: 'app-destaques',
  templateUrl: './destaques.component.html',
  styleUrls: ['./destaques.component.scss'],
  providers: [NgbCarouselConfig],
})
export class DestaquesComponent implements OnInit {
  private API_URL = environment.API_URL
  destaques: Array<Object>

  constructor(config: NgbCarouselConfig) {
    config.interval = 500000
    config.keyboard = true
    config.pauseOnHover = true
    this.destaques = []
  }

  ngOnInit(): void {
    get(`${this.API_URL}produtos`).then((response) => {
      response.data.forEach((data) => {
        // Populando array de destaques de acordo com os produtos com essa caracteróstica.
        if (data.destaque) this.destaques.push(data)
      })
    })
  }
}
