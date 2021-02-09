import { Component, OnInit } from '@angular/core'
import { environment } from '../../environments/environment'
import get from 'axios'
import { Produto } from '../produto_interface'
@Component({
  selector: 'app-produto',
  templateUrl: './produto.component.html',
  styleUrls: ['./produto.component.scss'],
})
export class ProdutoComponent implements OnInit {
  private API_URL = environment.API_URL
  private slipitedUrl = window.location.href.split('/')
  id: String
  produto: Produto

  constructor() {}

  ngOnInit(): void {
    this.id = this.slipitedUrl[this.slipitedUrl.length - 1]
    get(`${this.API_URL}produtos/${this.id}`).then((res) => {
      this.produto = res.data
      console.log(this.produto)
    })
  }
}
