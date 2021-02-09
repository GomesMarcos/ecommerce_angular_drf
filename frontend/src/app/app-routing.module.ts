import { importType } from '@angular/compiler/src/output/output_ast'
import { NgModule } from '@angular/core'
import { Routes, RouterModule } from '@angular/router'
import { ProdutoCardComponent } from './produto-card/produto-card.component'
import { ProdutoComponent } from './produto/produto.component'
import { NotFoundComponent } from './not-found/not-found.component'

const routes: Routes = [
  { path: '', component: ProdutoCardComponent },
  { path: 'produtos/:id', component: ProdutoComponent },
  { path: '**', component: NotFoundComponent },
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
