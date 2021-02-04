import { Component, OnInit } from '@angular/core'
import get from 'axios'
import { environment } from '../../environments/environment'

@Component({
  selector: 'app-produto-card',
  templateUrl: './produto-card.component.html',
  styleUrls: ['./produto-card.component.scss'],
})
export class ProdutoCardComponent implements OnInit {
  produtos: Array<Object>
  produtos_url: String = `${environment.API_URL}produtos`
  is_fetching: Boolean = true

  constructor() {}

  ngOnInit(): void {
    get(this.produtos_url.toString()).then((res) => {
      this.produtos = res.data
      this.is_fetching = false
    })
  }

  adicionarAoCarrinho(id) {
    console.log(id)
  }
}
