---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: security underwriting arrangement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: underwriting agreement between an organization (typically an investment bank) and a securities issuer that commits
      the underwriter to assuming risk involved in buying a new issue of securities and reselling it to the public
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Business and Economics Terms, Fifth Edition, 2012
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Sales may be made either directly or through third-party dealers.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/UnderwritingArrangement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/UnderwritingArrangement
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityUnderwritingArrangement
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: security underwriting arrangement
type: Ontology Class
---

# security underwriting arrangement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityUnderwritingArrangement>

## Definition

underwriting agreement between an organization (typically an investment bank) and a securities issuer that commits the underwriter to assuming risk involved in buying a new issue of securities and reselling it to the public

## Relationships

- **Subclass of**: [UnderwritingArrangement](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/UnderwritingArrangement.md)

## Constraints

- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [SecurityUnderwriter](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter.md)

## Annotations

- **label**: security underwriting arrangement
- **definition**: underwriting agreement between an organization (typically an investment bank) and a securities issuer that commits the underwriter to assuming risk involved in buying a new issue of securities and reselling it to the public
- **adaptedFrom**: Barron's Dictionary of Business and Economics Terms, Fifth Edition, 2012
- **explanatoryNote**: Sales may be made either directly or through third-party dealers.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
