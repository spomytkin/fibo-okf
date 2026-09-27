---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond conversion terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: terms indicating when a convertible bond can be converted to another security (usually a publicly traded share
      issued by of the same issuer)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ListedShare
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/specifiesConversionInto
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/ConversionTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ConversionTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondConversionTerms
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: bond conversion terms
type: Ontology Class
---

# bond conversion terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondConversionTerms>

## Definition

terms indicating when a convertible bond can be converted to another security (usually a publicly traded share issued by of the same issuer)

## Relationships

- **Subclass of**: [ConversionTerms](/concepts/fibo/SEC/Securities/SecuritiesIssuance/ConversionTerms.md)

## Constraints

- **[specifiesConversionInto](/concepts/fibo/SEC/Securities/SecuritiesIssuance/specifiesConversionInto.md)**: some values from of type [ListedShare](/concepts/fibo/SEC/Equities/EquityInstruments/ListedShare.md)

## Annotations

- **label**: bond conversion terms
- **definition**: terms indicating when a convertible bond can be converted to another security (usually a publicly traded share issued by of the same issuer)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
