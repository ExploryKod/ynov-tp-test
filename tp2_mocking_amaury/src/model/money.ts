import { Currency } from "./currency";

export class Money {
  constructor(readonly amount: number, readonly currency: Currency) {
  }
}