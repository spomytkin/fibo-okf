---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ticker symbol
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: reassignable identifier of relatively short character string length that is unique within an exchange for a particular
      financial instrument or listing for that instrument
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Every listed security has at least one unique ticker symbol, facilitating the vast array of trade orders that flow
      through the financial markets every day. However, in some countries this relationship may be indirect, through the listing,
      rather than direct, as is the case in the United States. In the US, the relationship between a ticker symbol and the
      listed security is one-to-one. This is not, however, the case in Singapore, where there may be unique ticker symbols
      for the same security based on the lot size. Some well-known ticker symbols are commonly used by multiple exchanges
      for the same instrument, such as 'IBM', though exchanges attempt to coordinate to limit duplication.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Ticker symbols are reusable, assigned to a given instrument by an exchange for some period of time.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
    value: N72f530857e8b4777840bcd5f870872d6
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.investopedia.com/terms/t/tickersymbol.asp
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.omg.org/spec/FIGI
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/IdentifiersAndIndices/ReassignableIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/ReassignableIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/TickerSymbol
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
title: ticker symbol
type: Ontology Class
---

# ticker symbol

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/TickerSymbol>

## Definition

reassignable identifier of relatively short character string length that is unique within an exchange for a particular financial instrument or listing for that instrument

## Relationships

- **See also**: [tickersymbol.asp](<https://www.investopedia.com/terms/t/tickersymbol.asp>)
- **See also**: [FIGI](<https://www.omg.org/spec/FIGI>)
- **Subclass of**: [ReassignableIdentifier](/concepts/fibo/FND/Arrangements/IdentifiersAndIndices/ReassignableIdentifier.md)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: some values from value `N72f530857e8b4777840bcd5f870872d6`

## Annotations

- **label**: ticker symbol
- **definition**: reassignable identifier of relatively short character string length that is unique within an exchange for a particular financial instrument or listing for that instrument
- **explanatoryNote**: Every listed security has at least one unique ticker symbol, facilitating the vast array of trade orders that flow through the financial markets every day. However, in some countries this relationship may be indirect, through the listing, rather than direct, as is the case in the United States. In the US, the relationship between a ticker symbol and the listed security is one-to-one. This is not, however, the case in Singapore, where there may be unique ticker symbols for the same security based on the lot size. Some well-known ticker symbols are commonly used by multiple exchanges for the same instrument, such as 'IBM', though exchanges attempt to coordinate to limit duplication.
- **usageNote**: Ticker symbols are reusable, assigned to a given instrument by an exchange for some period of time.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
