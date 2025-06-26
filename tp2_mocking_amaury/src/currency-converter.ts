import { Money } from "./model/money";
import { Currency } from "./model/currency";
import { ConversionRateApi } from "./external/conversion-rate-api";
import { CurrencyIsoCode } from "./external/currency-iso-code";

function codeToIsoCode(currency: Currency): CurrencyIsoCode {
  switch (currency) {
    case Currency.Euro:
      return CurrencyIsoCode.EUR;
    case Currency.Dollar:
      return CurrencyIsoCode.USD;
    case Currency.Pound:
      return CurrencyIsoCode.GBP;
    case Currency.Yen:
      return CurrencyIsoCode.JPY;
  }
}

export class CurrencyConverter {
  constructor(private readonly conversionRateApi: ConversionRateApi) {}

  sum(target: Currency, ...money: Money[]): Money {
    // We are paying each call we make to the API, so better not make useless calls
    let amount = 0;
    const knownRates = new Map<Currency, number>();
    knownRates.set(target, 1);

    for (const m of money) {
      const knownRate = knownRates.get(m.currency);
      if (!knownRate) {
        knownRates.set(
          m.currency,
          this.conversionRateApi.getRate(
            codeToIsoCode(m.currency),
            codeToIsoCode(target)
          )
        );
      }
      amount += m.amount * (knownRates.get(m.currency) || 0);
    }
    return new Money(amount, target);
  }
}
