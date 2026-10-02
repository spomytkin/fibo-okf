---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund investment restrictions set
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Limitations that apply to the fund as a whole, such as risk factors. these are used to determine whether the fund
      is appropriate for a given type of investor to invest in.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These are defined by the overall Fund investment policy. Not the same as the detailed policies for investing in
      percentages of this or that.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/Prospectus
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isPartOf
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/InvestmentRestriction
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund investment restrictions set
type: Ontology Class
---

# fund investment restrictions set

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/InvestmentRestriction>

## Definition

Limitations that apply to the fund as a whole, such as risk factors. these are used to determine whether the fund is appropriate for a given type of investor to invest in.

## Relationships

- **Subclass of**: [SecuritiesRestriction](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md)

## Constraints

- **[isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)**: some values from of type [Prospectus](/concepts/fibo/SEC/Securities/SecuritiesIssuance/Prospectus.md)

## Annotations

- **label** (en): fund investment restrictions set
- **definition** (en): Limitations that apply to the fund as a whole, such as risk factors. these are used to determine whether the fund is appropriate for a given type of investor to invest in.
- **explanatoryNote** (en): These are defined by the overall Fund investment policy. Not the same as the detailed policies for investing in percentages of this or that.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
