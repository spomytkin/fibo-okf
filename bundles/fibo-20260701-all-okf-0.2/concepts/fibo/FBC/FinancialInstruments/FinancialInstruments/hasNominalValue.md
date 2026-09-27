---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has nominal value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the face value of a contract
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Nominal value of a security is its redemption price and will vary from its market value. A preferred stock's nominal
      (par) value is important in that it is used to calculate its dividend while the nominal value of common stock is an
      arbitrary value assigned for balance sheet purposes.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: "The nominal amount of a financial instrument is the face amount used to calculate payments made on that instrument.\
      \ This amount generally does not change.\n\t\t\n\t\tFor securities the nominal value is often referred to as the face\
      \ or par value. This is the redemption price of the security and is normally stated on the front of that security. With\
      \ respect to bonds and stocks, it is the stated value of an issued security, as opposed to its market value."
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has face value
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
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasNominalValue
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: has nominal value
type: Ontology Property
---

# has nominal value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasNominalValue>

## Definition

indicates the face value of a contract

## Relationships

- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label**: has nominal value
- **definition**: indicates the face value of a contract
- **explanatoryNote**: Nominal value of a security is its redemption price and will vary from its market value. A preferred stock's nominal (par) value is important in that it is used to calculate its dividend while the nominal value of common stock is an arbitrary value assigned for balance sheet purposes.
- **explanatoryNote**: The nominal amount of a financial instrument is the face amount used to calculate payments made on that instrument. This amount generally does not change. 		 		For securities the nominal value is often referred to as the face or par value. This is the redemption price of the security and is normally stated on the front of that security. With respect to bonds and stocks, it is the stated value of an issued security, as opposed to its market value.
- **synonym**: has face value

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
