---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: industry sector classifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: standardized classification or delineation for an organization, or possibly for a security representing an interest
      in a given organization, per some scheme for such delineation, by industry
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier
sources:
- id: fibo-source-7338de6177
  resource: references/fibo/FND/Arrangements/ClassificationSchemes.rdf
  sha256: 7338de61776faa661146c3b44c6902fc98da670de604e69439fae05577135627
  title: FIBO source FND/Arrangements/ClassificationSchemes.rdf
title: industry sector classifier
type: Ontology Class
---

# industry sector classifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier>

## Definition

standardized classification or delineation for an organization, or possibly for a security representing an interest in a given organization, per some scheme for such delineation, by industry

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: exact qualified cardinality 1 of type [IndustrySectorClassificationScheme](/concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme.md)

## Annotations

- **label**: industry sector classifier
- **definition**: standardized classification or delineation for an organization, or possibly for a security representing an interest in a given organization, per some scheme for such delineation, by industry

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
