---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has notional amount
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: has a generally unchangeable value used for certain calculations, expressed as some monetary amount
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code,
      Fourth Edition, 2019-10, clause 6.8.2
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For certain kinds of derivative instruments, including but not limited to swaps, the notional amount indicates
      face amount of a swap upon which the payment streams for that swap are based. While this is typically constant throughout
      the lifetime of a contract, it can be accreting, amortizing, or custom, such as in the case of a notional step schedule.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: "The notional amount (or notional principal amount or notional value) on a financial instrument is typically the\
      \ face amount used to calculate payments made on that instrument. This amount generally does not change and is thus\
      \ referred to as notional.\n\t\t\n\t\tWhen applied to a swap this is the amount used for calculating the actual value\
      \ of the interest due. Also known as notional value when describing derivative contracts in the options, futures, and\
      \ currency markets, this term is often used to value the underlying asset in a derivatives trade. It can be the total\
      \ value of a position, how much value a position controls, or an agreed-upon amount in a contract.\n\n\t\tAn example\
      \ is that a firm might have a variable rate loan on $100,000 but decide to swap only $40,000. The $40,000 is the notional\
      \ amount of the swap and becomes the amount on which interest is paid."
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNotionalAmount
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: has notional amount
type: Ontology Property
---

# has notional amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNotionalAmount>

## Definition

has a generally unchangeable value used for certain calculations, expressed as some monetary amount

## Relationships

- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label**: has notional amount
- **definition**: has a generally unchangeable value used for certain calculations, expressed as some monetary amount
- **adaptedFrom**: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019-10, clause 6.8.2
- **explanatoryNote**: For certain kinds of derivative instruments, including but not limited to swaps, the notional amount indicates face amount of a swap upon which the payment streams for that swap are based. While this is typically constant throughout the lifetime of a contract, it can be accreting, amortizing, or custom, such as in the case of a notional step schedule.
- **explanatoryNote**: The notional amount (or notional principal amount or notional value) on a financial instrument is typically the face amount used to calculate payments made on that instrument. This amount generally does not change and is thus referred to as notional. 		 		When applied to a swap this is the amount used for calculating the actual value of the interest due. Also known as notional value when describing derivative contracts in the options, futures, and currency markets, this term is often used to value the underlying asset in a derivatives trade. It can be the total value of a position, how much value a position controls, or an agreed-upon amount in a contract.  		An example is that a firm might have a variable rate loan on $100,000 but decide to swap only $40,000. The $40,000 is the notional amount of the swap and becomes the amount on which interest is paid.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
