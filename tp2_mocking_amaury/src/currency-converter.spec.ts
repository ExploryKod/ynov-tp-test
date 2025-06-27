import { CurrencyConverter } from "./currency-converter";
import { Currency } from "./model/currency";
import { Money } from "./model/money";
import { CurrencyIsoCode } from "./external/currency-iso-code";
import { ConversionRateApi } from "./external/conversion-rate-api";
import { codeToIsoCode } from "./currency-converter";

class MockConversionRateApi extends ConversionRateApi {
  private rates = new Map<string, number>();

  setRate(source: CurrencyIsoCode, target: CurrencyIsoCode, rate: number) {
    this.rates.set(`${source}->${target}`, rate);
  }

 override getRate(source: CurrencyIsoCode, target: CurrencyIsoCode): number {
  const key = `${source}->${target}`;
  const rate = this.rates.get(key);
  console.log(`Mock API getRate from ${source} to ${target}: ${rate}`); 
  if (rate === undefined) {
    throw new Error(`Missing fake rate for ${key}`);
  }
  return rate;
}

}


describe("codeToIsoCode", () => {
  it.each([
    [Currency.Euro, CurrencyIsoCode.EUR],
    [Currency.Dollar, CurrencyIsoCode.USD],
    [Currency.Pound, CurrencyIsoCode.GBP],
    [Currency.Yen, CurrencyIsoCode.JPY],
  ])("maps %s to %s", (currency, expectedIso) => {
    expect(codeToIsoCode(currency)).toBe(expectedIso);
  });
});


describe("CurrencyConverter", function () {
  it("is initialized", () => {
    const converter = new CurrencyConverter(new ConversionRateApi());
    expect(converter).toBeTruthy();
  });

  it("throws if the real API is called", () => {
    const converter = new CurrencyConverter(new ConversionRateApi());

    expect(() => {
      converter.sum(
        Currency.Euro,
        new Money(2, Currency.Dollar)
      );
    }).toThrowError(
      "401 - Unauthorized, IP not recognized. Are you trying to call us via a unit test?"
    );
  });

  it("converts and sums amounts", () => {
    const fakeApi = new MockConversionRateApi();
    fakeApi.setRate(CurrencyIsoCode.USD, CurrencyIsoCode.EUR, 0.9);

    const converter = new CurrencyConverter(fakeApi);

    const result = converter.sum(
      Currency.Euro,
      new Money(2, Currency.Dollar)
    );

    expect(result.currency).toBe(Currency.Euro);
    expect(result.amount).toBeCloseTo(1.8);
  });

  it("sums multiple currencies", () => {
    const fakeApi = new MockConversionRateApi();
    fakeApi.setRate(CurrencyIsoCode.USD, CurrencyIsoCode.EUR, 0.9);
    fakeApi.setRate(CurrencyIsoCode.GBP, CurrencyIsoCode.EUR, 1.1);

    const converter = new CurrencyConverter(fakeApi);

    const result = converter.sum(
      Currency.Euro,
      new Money(2, Currency.Dollar),  
      new Money(3, Currency.Pound)    
    );

    expect(result.currency).toBe(Currency.Euro);
    expect(result.amount).toBeCloseTo(1.8 + 3.3);
  });

  it("converts dollars to euros", () => {
  const fakeApi = new MockConversionRateApi();
  fakeApi.setRate(CurrencyIsoCode.USD, CurrencyIsoCode.EUR, 0.9);
  const converter = new CurrencyConverter(fakeApi);

  const result = converter.sum(
    Currency.Euro,
    new Money(10, Currency.Dollar)
  );

  expect(result.amount).toBe(9);
  expect(result.currency).toBe(Currency.Euro);
});

it.each([
  [Currency.Euro, Currency.Dollar, 1.5, 10, 15],
  [Currency.Dollar, Currency.Euro, 0.8, 20, 16],
  [Currency.Yen, Currency.Euro, 0.007, 1000, 7],
])(
  "converts %d %s to %s with rate %f results in %d",
  (source, target, rate, amount, expected) => {
    const fakeApi = new MockConversionRateApi();
    fakeApi.setRate(codeToIsoCode(source), codeToIsoCode(target), rate);
    const converter = new CurrencyConverter(fakeApi);

    const result = converter.sum(
      target,
      new Money(amount, source)
    );

    expect(result.amount).toBeCloseTo(expected);
    expect(result.currency).toBe(target);
  }
);

});


