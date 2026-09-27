---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: private offering
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: offering of securities made privately to a limited number of qualified potential investors
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: EDM Council / Quarule
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Unlike a public offering, a private placement does not have to be registered with a regulatory agency if the securities
      are purchased for investment rather than resale.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: private placement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/PrivatePlacementMemorandum
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidencedBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecuritiesOffering
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/PrivateOffering
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: private offering
type: Ontology Class
---

# private offering

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/PrivateOffering>

## Definition

offering of securities made privately to a limited number of qualified potential investors

## Relationships

- **Subclass of**: [SecuritiesOffering](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md)

## Constraints

- **[isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)**: some values from of type [PrivatePlacementMemorandum](/concepts/fibo/SEC/Securities/SecuritiesIssuance/PrivatePlacementMemorandum.md)

## Annotations

- **label**: private offering
- **definition**: offering of securities made privately to a limited number of qualified potential investors
- **adaptedFrom**: EDM Council / Quarule
- **explanatoryNote**: Unlike a public offering, a private placement does not have to be registered with a regulatory agency if the securities are purchased for investment rather than resale.
- **synonym**: private placement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
