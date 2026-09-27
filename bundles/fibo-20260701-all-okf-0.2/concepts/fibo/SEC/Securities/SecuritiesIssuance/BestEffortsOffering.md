---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: best efforts offering
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: securities offering whereby investment bankers commit to doing their best to sell the securities offered, but do
      not assume the full risk of an underwriter
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In a best efforts offering, the agreement is strictly an agency arrangement, with no obligation on the part of
      the agent to purchase the securities. They act as a broker, in other words.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecuritiesOffering
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/BestEffortsOffering
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: best efforts offering
type: Ontology Class
---

# best efforts offering

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/BestEffortsOffering>

## Definition

securities offering whereby investment bankers commit to doing their best to sell the securities offered, but do not assume the full risk of an underwriter

## Relationships

- **Subclass of**: [SecuritiesOffering](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md)

## Annotations

- **label**: best efforts offering
- **definition**: securities offering whereby investment bankers commit to doing their best to sell the securities offered, but do not assume the full risk of an underwriter
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
- **explanatoryNote**: In a best efforts offering, the agreement is strictly an agency arrangement, with no obligation on the part of the agent to purchase the securities. They act as a broker, in other words.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
