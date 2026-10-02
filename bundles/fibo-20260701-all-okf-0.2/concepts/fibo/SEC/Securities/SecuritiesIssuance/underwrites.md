---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: underwrites
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies one or more underwriters involved in raising capital for or distributing the instruments that are the
      subject of the offering
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investopedia.com/terms/u/underwriting.asp
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Underwriting is the process by which investment bankers raise investment capital from investors on behalf of corporations
      and governments that are issuing either equity or debt securities.
  domain:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter
  inverse_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/isUnderwrittenBy.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isUnderwrittenBy
  range:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecuritiesOffering
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/underwrites
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: underwrites
type: Ontology Property
---

# underwrites

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/underwrites>

## Definition

identifies one or more underwriters involved in raising capital for or distributing the instruments that are the subject of the offering

## Relationships

- **Domain**: [Underwriter](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md)
- **Inverse of**: [isUnderwrittenBy](/concepts/fibo/SEC/Securities/SecuritiesIssuance/isUnderwrittenBy.md)
- **Range**: [SecuritiesOffering](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md)

## Annotations

- **label**: underwrites
- **definition**: identifies one or more underwriters involved in raising capital for or distributing the instruments that are the subject of the offering
- **adaptedFrom**: http://www.investopedia.com/terms/u/underwriting.asp
- **explanatoryNote**: Underwriting is the process by which investment bankers raise investment capital from investors on behalf of corporations and governments that are issuing either equity or debt securities.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
