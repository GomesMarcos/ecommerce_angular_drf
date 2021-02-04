import { BrowserModule } from '@angular/platform-browser'
import { NgModule } from '@angular/core'

import { AppRoutingModule } from './app-routing.module'
import { AppComponent } from './app.component'
import { DestaquesComponent } from './destaques/destaques.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ProdutoCardComponent } from './produto-card/produto-card.component';
import { FetchComponent } from './fetch/fetch.component'

@NgModule({
  declarations: [AppComponent, DestaquesComponent, ProdutoCardComponent, FetchComponent],
  imports: [BrowserModule, AppRoutingModule, NgbModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
