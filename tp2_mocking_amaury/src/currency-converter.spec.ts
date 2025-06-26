import { ConversionRateApi } from "./external/conversion-rate-api";
import { CurrencyConverter } from "./currency-converter";
import { Currency } from "./model/currency";
import { Money } from "./model/money";

describe("CurrencyConverter", function () {
  it("is initialized", () => {
    const converter = new CurrencyConverter(new ConversionRateApi());
    expect(converter).toBeTruthy();
  });
  it("does not work (TODO!)", () => {
    const converter = new CurrencyConverter(new ConversionRateApi());

    converter.sum(Currency.Euro, new Money(2, Currency.Dollar));
  });
});
